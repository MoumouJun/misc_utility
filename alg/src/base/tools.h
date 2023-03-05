#ifndef _TOOLS_H_
#define _TOOLS_H_

#include "base.h"

#include <elog.h>


/* set EasyLogger log format */
#define ELOG_FMT_DEBUD (ELOG_LVL_ERROR, ELOG_FMT_TAG | ELOG_FMT_TIME | ELOG_FMT_LVL | ELOG_FMT_DIR | ELOG_FMT_LINE)
#define ELOG_FMT (ELOG_LVL_ERROR, ELOG_FMT_TAG | ELOG_FMT_TIME | ELOG_FMT_LVL)

class CTools
{
public:
    CTools() {}
    ~CTools()
    {
        // 日志库异步刷新
        fflush(stdout);
        sleep(0);
    }

public:
    void start()
    {
        // 日志工具初始化
        elogInit();
    }

    void elogInit()
    {
        /* initialize EasyLogger */
        elog_init();

        elog_set_fmt(ELOG_LVL_ASSERT, ELOG_FMT_DEBUD);
        elog_set_fmt(ELOG_LVL_ERROR, ELOG_FMT);
        elog_set_fmt(ELOG_LVL_WARN, ELOG_FMT);
        elog_set_fmt(ELOG_LVL_INFO, ELOG_FMT);
        elog_set_fmt(ELOG_LVL_DEBUG, ELOG_FMT_DEBUD);
        elog_set_fmt(ELOG_LVL_VERBOSE, ELOG_FMT_DEBUD);
        elog_set_text_color_enabled(true);
        /* start EasyLogger */
        elog_start();
    }

private:
};

class C_Test_Tools
{
public:
    void init_elog(void)
    {
    }

    static void test_elog(void)
    {
        /* initialize EasyLogger */
        elog_init();
        elog_set_fmt(ELOG_LVL_ASSERT, ELOG_FMT_DEBUD);
        elog_set_fmt(ELOG_LVL_ERROR, ELOG_FMT);
        elog_set_fmt(ELOG_LVL_WARN, ELOG_FMT);
        elog_set_fmt(ELOG_LVL_INFO, ELOG_FMT);
        elog_set_fmt(ELOG_LVL_DEBUG, ELOG_FMT_DEBUD);
        elog_set_fmt(ELOG_LVL_VERBOSE, ELOG_FMT_DEBUD);
        elog_set_text_color_enabled(true);
        /* start EasyLogger */
        elog_start();

        /* test log output for all level */
        // log_a("Hello EasyLogger!");
        log_v("init","Hello EasyLogger!");
        log_e("init","Hello EasyLogger!");
        log_w("init","Hello EasyLogger!");
        log_i("init","Hello EasyLogger!");
        log_d("init","Hello EasyLogger!");
        log_v("init","Hello EasyLogger!");

        fflush(stdout);
        // sleep(0);
        //    elog_raw("Hello EasyLogger!");
    }
};

#endif