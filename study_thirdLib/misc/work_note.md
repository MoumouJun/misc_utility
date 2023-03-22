## 知识点

1. 负载： CPU、内存、磁盘/网络等 IO
   _命令行工具_：
   **w**
   一行负载（1/5/15 分钟的平均负载，系统的持续运行时间，登录的用户数以及正在进行的操作
   **uptime**
   显示系统运行时间以及当前负载
   **top** [各字段详解](https://www.cnblogs.com/zhoug2020/p/6336453.html)
2. inode
   一切接文件 设备无关性
   https://blog.csdn.net/yuexiaxiaoxi27172319/article/details/45241923#:~:text=Linux%E6%94%AF%E6%8C%81%E5%A4%9A%E7%A7%8D%E6%96%87%E4%BB%B6,%E7%95%8C%E9%9D%A2%E5%92%8C%E5%BA%94%E7%94%A8%E7%BC%96%E7%A8%8B%E6%8E%A5%E5%8F%A3%E3%80%82
    https://www.cnblogs.com/llife/p/11470668.html

```c
// < linux/fs.h >
struct inode {
        struct hlist_node       i_hash;              /* hash list */
        struct list_head        i_list;              /* list of inodes */
        struct list_head        i_dentry;            /* list of dentries */
        unsigned long           i_ino;               /* inode number */
        atomic_t                i_count;             /* reference counter */
        umode_t                 i_mode;              /* access permissions */
        unsigned int            i_nlink;             /* number of hard links */
        uid_t                   i_uid;               /* user id of owner */
        gid_t                   i_gid;               /* group id of owner */
        kdev_t                  i_rdev;              /* real device node */
        loff_t                  i_size;              /* file size in bytes */
        struct timespec         i_atime;             /* last access time */
        struct timespec         i_mtime;             /* last modify time */
        struct timespec         i_ctime;             /* last change time */
        unsigned int            i_blkbits;           /* block size in bits */
        unsigned long           i_blksize;           /* block size in bytes */
        unsigned long           i_version;           /* version number */
        unsigned long           i_blocks;            /* file size in blocks */
        unsigned short          i_bytes;             /* bytes consumed */
        spinlock_t              i_lock;              /* spinlock */
        struct rw_semaphore     i_alloc_sem;         /* nests inside of i_sem */
        struct semaphore        i_sem;               /* inode semaphore */
        struct inode_operations *i_op;               /* inode ops table */
        struct file_operations  *i_fop;              /* default inode ops */
        struct super_block      *i_sb;               /* associated superblock */
        struct file_lock        *i_flock;            /* file lock list */
        struct address_space    *i_mapping;          /* associated mapping */
        struct address_space    i_data;              /* mapping for device */
        struct dquot            *i_dquot[MAXQUOTAS]; /* disk quotas for inode */
        struct list_head        i_devices;           /* list of block devices */
        struct pipe_inode_info  *i_pipe;             /* pipe information */
        struct block_device     *i_bdev;             /* block device driver */
        unsigned long           i_dnotify_mask;      /* directory notify mask */
        struct dnotify_struct   *i_dnotify;          /* dnotify */
        unsigned long           i_state;             /* state flags */
        unsigned long           dirtied_when;        /* first dirtying time */
        unsigned int            i_flags;             /* filesystem flags */
        unsigned char           i_sock;              /* is this a socket? */
        atomic_t                i_writecount;        /* count of writers */
        void                    *i_security;         /* security module */
        __u32                   i_generation;        /* inode version number */
        union {
                void            *generic_ip;         /* filesystem-specific info */
        } u;
};
struct inode_operations {
        int (*create) (struct inode *, struct dentry *,int);
        struct dentry * (*lookup) (struct inode *, struct dentry *);
        int (*link) (struct dentry *, struct inode *, struct dentry *);
        int (*unlink) (struct inode *, struct dentry *);
        int (*symlink) (struct inode *, struct dentry *, const char *);
        int (*mkdir) (struct inode *, struct dentry *, int);
        int (*rmdir) (struct inode *, struct dentry *);
        int (*mknod) (struct inode *, struct dentry *, int, dev_t);
        int (*rename) (struct inode *, struct dentry *,
                       struct inode *, struct dentry *);
        int (*readlink) (struct dentry *, char *, int);
        int (*follow_link) (struct dentry *, struct nameidata *);
        int (*put_link) (struct dentry *, struct nameidata *);
        void (*truncate) (struct inode *);
        int (*permission) (struct inode *, int);
        int (*setattr) (struct dentry *, struct iattr *);
        int (*getattr) (struct vfsmount *, struct dentry *, struct kstat *);
        int (*setxattr) (struct dentry *, const char *,
                         const void *, size_t, int);
        ssize_t (*getxattr) (struct dentry *, const char *, void *, size_t);
        ssize_t (*listxattr) (struct dentry *, char *, size_t);
        int (*removexattr) (struct dentry *, const char *);
};
```

3. 红黑树与 AVL 树
   1. https://www.zhihu.com/question/19856999
   2. https://zhuanlan.zhihu.com/p/93369069
   3. https://blog.51cto.com/u_15077537/4201553
4. git 钩子

   1. https://juejin.cn/post/6844903521393852424
   2. https://git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-Git-%E9%92%A9%E5%AD%90

5. 递归
   1. https://zhuanlan.zhihu.com/p/94748605
6. yield 与 sleep （Linux内核API）
   1. https://stackoverflow.com/questions/5304324/whats-the-difference-between-yield-and-sleep
   2. https://deepinout.com/linux-kernel-api/linux-kernel-api-process-scheduling/linux-kernel-api-yield.html
7. Linux 源码分版本在线
   1. https://elixir.bootlin.com/linux/latest/source

## 源码仓库

1. python
   1. [CPython-Internals（cpython 源码分析） ](https://github.com/zpoint/CPython-Internals)
   2. [cpython 源码分析 入门](https://zhuanlan.zhihu.com/p/79656976)
2. 操作系统
   1. [freeRTOS 内核源码](https://github.com/FreeRTOS/FreeRTOS-Kernel)
   2. [freeRTOS 支持tcp](https://github.com/FreeRTOS/FreeRTOS-Plus-TCP)
   3.