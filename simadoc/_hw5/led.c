/********************************************************
 * led.h
 *
 * this file provides function implementation for SER486
 * led library functions.
 *
 * Author:   Doug Sandy
 * Date:     2/16/2018
 * Revision: 1.0
 *
 * Copyright(C) 2018, Arizona State University
 * All rights reserved
 *
 */
#include "delay.h"

#define DDRB (*((volatile unsigned char *)0x24))
#define PORTB (*((volatile unsigned char *)0x25))

    volatile unsigned char *pddrb = (volatile unsigned char *)0x24;

/*************************************************
* init()
*
* initialize the LED port pin direction and turn
* off the LED.
*
* parameters:
*   none
*
* returns:
*   none
*
* changes:
*   the value of the PORTB and DDRB bit 1 may
*   change.
*
* Note: Care is taken to ensure that no other bits
*   in the registers are not altered.  Atomic
*   operations are used so this code is interrupt-
*   safe.
*/
void led_init()
{
    /* set the data direction bit (port $03 = 0x23 = DDRB */
    DDRB |= 0x02;

    /* turn off the LED if it is on (port $05 = 0x25 = PORTB */
    PORTB &= 0xFD;
}

/*************************************************
* on()
*
* turn on the LED.
*
* parameters:
*   none
*
* returns:
*   none
*
* changes:
*   the value of the PORTB may change.
*
* Note: Care is taken to ensure that no other bits
*   in the registers are not altered.  Atomic
*   operations are used so this code is interrupt-
*   safe.
*/
void led_on()
{
    /* turn on the LED (port $05 = 0x25 = PORTB */
    PORTB |= 0x02;
}

/*************************************************
* off()
*
* turn off the LED.
*
* parameters:
*   none
*
* returns:
*   none
*
* changes:
*   the value of the PORTB may change.
*
* Note: Care is taken to ensure that no other bits
*   in the registers are not altered.  Atomic
*   operations are used so this code is interrupt-
*   safe.
*/
void led_off()
{
    /* turn off the LED (port $05 = 0x25 = PORTB */
    PORTB &= 0xFD;
}

/*************************************************
* ison()
*
* returns the status of the LED - 1 if on, 0 if off.
*
* parameters:
*   none
*
* returns:
*   1 if the LED is on, otherwise 0.
*
* changes:
*   nothing
*
* Note: Care is taken to ensure that no other bits
*   in the registers are not altered.  Atomic
*   operations are used so this code is interrupt-
*   safe.
*/
int  led_ison()
{
    return (PORTB>>1)&1;
}

/*************************************************
* led_blink()
*
* given an ascii null terminated string, this function
* blinks the morse code representation of the string.
* '-' characters will blink a long led pulse. '.'
* characters will blink a short led pulse.  Space
* characters will delay.  All other characters will
* be ignored.
*
* parameters:
*   msg - an ascii null terminated string of Morse code
*         to output to the LED.
*
* returns:
*   none
*
* changes:
*   the value of the PORTB and DDRB bit 1 may
*   change.
*
* Note: Care is taken to ensure that no other bits
*   in the registers are not altered.  Atomic
*   operations are used so this code is interrupt-
*   safe.
*/
void led_blink(char *msg)
{
    unsigned int i;

    /* turn off the led if it is not already off */
    led_off();

    for (i=0; msg[i]!=0; i++)
    {
        if (msg[i]=='.')
        {
            /* output a Morse code di (short pulse) */
            led_on();    /* turn led on for a short period */
            delay(250);

            led_off();   /* turn led off for a slight pause */
            delay(100);
        } else if (msg[i]=='-')
        {
            /* output a Morse code dah (long pulse) */
            led_on();    /* turn led on for a long period */
            delay(750);

            led_off();   /* turn led off for a slight pause */
            delay(100);

        } else if (msg[i]==' ')
        {
            /* output a break (delay with no pulse) */
            delay(1000); /* leave led off for a long period */
        }
    }
}
