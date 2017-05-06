init 410 python:
    config.label_overrides["splashscreen"] = "lb__test_start"

    GLOBAL_LB_TEST_BAR_VALUE = 0
    GLOBAL_LB_TEST_BAR_MAX   = 30

    def lb__test_bgprocess():
        global GLOBAL_LB_TEST_BAR_VALUE
        for i in range(GLOBAL_LB_TEST_BAR_MAX):
            import time
            time.sleep(0.1)
            GLOBAL_LB_TEST_BAR_VALUE += 1
            renpy.restart_interaction()

screen lb__test_progress:
    hbox pos (0.5, 0.5) anchor (0.5, 0.5):
        hbox xminimum 0.5 xmaximum 0.5:
            bar value GLOBAL_LB_TEST_BAR_VALUE range GLOBAL_LB_TEST_BAR_MAX
        label "%d/%d" % (GLOBAL_LB_TEST_BAR_VALUE, GLOBAL_LB_TEST_BAR_MAX)
    if  GLOBAL_LB_TEST_BAR_VALUE != GLOBAL_LB_TEST_BAR_MAX:
        label "Please wait..." pos (0.5, 0.45) anchor (0.5, 0.5)
    else:
        label "Press DONE button to continue" pos (0.5, 0.45) anchor (0.5, 0.5)
        button pos (0.5, 0.6) anchor (0.5, 0.5) clicked ui.jumps("lb__test_done"):
            label "DONE" text_size 64

label lb__test_start:
    "start"
    $ renpy.invoke_in_thread(lb__test_bgprocess)
    jump lb__test_loop

label lb__test_loop:
    show screen lb__test_progress
    $ ui.interact()
    jump lb__test_loop

label lb__test_done:
    hide screen lb__test_progress
    "done"
