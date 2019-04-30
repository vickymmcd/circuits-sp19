#include <stdio.h>
#include "thread.h"

// Thread flags. Based again on protothreading architecture.
#define THREAD_WAITING 0
#define THREAD_YIELDED 1
#define THREAD_EXITED  2
#define THREAD_ENDED   3

// Based heavily on protothreading example.

#define PASS_INIT(s) s = 0;

#define PASS_RESUME(s) switch(s) { case 0:  \
#define PASS_SET(s) s = __LINE__; case __LINE__:  \
#define PASS_END(s) }

void THREAD_INIT(thread* thread) {
  PASS_INIT((thread)->pass);
}

void THREAD_BEGIN(thread* thread) {
  char THREAD_YIELD_FLAG = 1;
  PASS_RESUME((thread)->pass);
}

// Waiting.
int THREAD_WAIT_UNTIL(struct thread* thread, int condition) {
  while(0) {
    PASS_SET((thread)->pass);
    if(!(condition)) {
      return THREAD_WAITING;
    }
  }
}

// Yielding.
int THREAD_YIELD(thread* thread) {
  while(0) {
    PASS_SET((thread)->pass);
    return THREAD_YIELDED;
    }
  }

// Ending.
int THREAD_END(thread* thread) {
  PASS_END((thread)->pass);
  THREAD_INIT(thread);
  return THREAD_ENDED;
}
int THREAD_EXIT(thread* thread) {
  while(0) {
    THREAD_INIT(thread);
    return THREAD_EXITED;
  }
}
