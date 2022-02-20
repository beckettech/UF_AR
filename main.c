#include "msp.h"
/**
 * main.c
 */

void SysTickInit()
{
    SysTick->CTRL = 0x00000005;           // enable SysTick with no interrupts
}

void SysTick_Wait(uint32_t n)
{
    SysTick->LOAD = n-1;
    SysTick->VAL = 0; // clear Count
    while((SysTick->CTRL&0x00010000)== 0){};
}

void wait_ms(uint16_t ms)
{
    uint16_t counter;
    for(counter = 0; counter < ms; counter++)
    {
        SysTick_Wait(48*1000);
    }
}

void wait_seconds(uint16_t seconds)
{
    uint16_t counter;
    for(counter = 0; counter < seconds; counter++)
    {
        wait_ms(1000);
    }
}

void wait_us(uint16_t us)
{
    uint16_t counter;
    for(counter = 0; counter < us; counter++)
    {
        SysTick_Wait(48);
    }
}

void initMotors(void)
{
    P1->DIR |= 0b11000000;
    P2->DIR |= 0b11000000;
    P3->DIR |= 0b11000000;

    //Turn off sleep
    P3->OUT |= 0b11000000;
}

void runMotors(uint16_t duty, uint32_t seconds)
{
    uint32_t counter;
    for(counter = 0; counter < seconds * 4000; counter++)
    {
        turnMotorsOn();
        wait_us(duty);
        turnMotorsOff();
        wait_us(100-duty);
    }
}

void turnMotorsOn(void)
{
    P1->OUT |= 0b11000000;
    P2->OUT |= 0b11000000;
}

void turnMotorsOff(void)
{
    P1->OUT &= 0b00111111;
    P2->OUT &= 0b00111111;
}

void main(void)
{
     WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;		// stop watchdog timer
     Clock_Init48MHz();
     SysTickInit();
     initMotors();
     wait_seconds(1);
     runMotors(75, 1);
     while(1){}
}
