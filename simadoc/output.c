/********************************************************
 * output.c
 *
 * SER486 Assignment 4
 * Spring 2018
 * Written By:  Doug Sandy (instructor)
 * Modified By:
 *
 * this file implements functions associated with SER486
 * homework assignment 4.  The procedures implemented
 * provide led and console output support for debugging
 * of future SER 486 assignments.
 *
 * functions are:
 *    writestr(char *)  - a function to write an ascii
 *                        null-terminated string to the
 *                        avr atmega 328P uart port.
 *                        (instructor provided)
 *
 *    writehex8(unsigned char) - a function to write the
 *                        hexadecimal representation of
 *                        an 8-bit unsigned integer to
 *                        avr atmega 328P uart port.
 *
 *    writehex16(unsigned int) - a function to write the
 *                        hexadecimal representation of
 *                        a 16-bit unsigned integer to
 *                        avr atmega 328P uart port.
 *
 *    blink_led(char *) - a function to send a specific
 *                        blink pattern to the development
 *                        board's user-programmable LED.
 *
 *    delay(unsigned int) - delay code execution for
 *                        the specified amount of milliseconds.
 *                        (instructor provided)
 */

 #include "hw4lib.h"

 /* macro definitions used by delay() */
 #define MSEC_PER_SEC     1000
 #define CLOCKS_PER_LOOP  16
 #define LOOPS_PER_MSEC   ((F_CPU/MSEC_PER_SEC)/CLOCKS_PER_LOOP)

/**********************************
 * delay(unsigned int msec)
 *
 * This code delays execution for for
 * the specified amount of milliseconds.
 *
 * arguments:
 *   msec - the amount of milliseconds to delay
 *
 * returns:
 *   nothing
 *
 * changes:
 *   nothing
 *
 * NOTE: this is not ideal coding practice since the
 * amount of time spent in this delay may change with
 * future hardware changes.  Ideally a timer should be
 * used instead of a set of for loops.  Timers will be
 * taught later in the semester.
 */
void delay(unsigned int msec)
{
    volatile unsigned i,j ;  /* volatile prevents loops from being optimized away */

    /* outer loop, loops for specified number of milliseconds */
    for (i=0; i<msec; i++) {
        /* inner loop, loops for 1 millisecond delay */
        for (j=0;j<LOOPS_PER_MSEC;j++) {}
    }
}


/**********************************
 * writestr(char * str)
 *
 * This code writes a null-terminated string
 * to the UART.
 *
 * arguments:
 *   str - a pointer to the beginning of the
 *         string to be printed.
 *
 * returns:
 *   nothing
 *
 * changes:
 *   the state of the uart transmit buffer will
 *   be changed by this function.
 *
 * NOTE: uart_init() should be called this function
 *   is invoked for the first time or unpredictable
 *   UART behavior may result.
 */
void writestr(char * str)
{
    unsigned int i;

    /* loop for each character in the string */
    for (i=0; str[i]!=0;i++) {
        /* output the character to the UART */
        uart_writechar(str[i]);
    }
}

void writehex8(unsigned char num)
{
    signed char i;
    unsigned char ch;

    /* loop for each nibble in the byte */
    for (i=4;i>=0;i-=4) {
        /* extract a single nibble */
        ch = ((num>>i)&0xf);
        /* convert to ascii hex digit */
        (ch>9) ? (ch = ch + 'A' - 10) : (ch = ch +'0');
        uart_writechar(ch);
    }
}

void writehex16(unsigned int num)
{
    signed char i;
    unsigned char ch;
    /* loop for each byte in the word */
    for (i=8;i>=0;i-=8) {
        /* extract a single nibble */
        ch = (unsigned char)((num>>i)&0xff);
        /* convert to ascii hex digit */
        writehex8(ch);
    }
}

void blink_led(char *msg)
{
    volatile unsigned char *ppinb = (volatile unsigned char *)0x23;
    volatile unsigned char *pddrb = (volatile unsigned char *)0x24;
    unsigned int i;

    /* make sure the direction of the led pin is set to output */
    *pddrb |= 0x2;

    /* turn off the led if it is not already off */
    if ((*ppinb)&0x2) *ppinb|=0x2;

    for (i=0; msg[i]!=0; i++)
    {
        if (msg[i]=='.')
        {
            /* turn led on for a short period */
            *ppinb |= 0x2;
            delay(250);

            /* turn led off for a slight pause */
            *ppinb |= 0x2;
            delay(100);

        } else if (msg[i]=='-')
        {
            /* turn led on for a long period */
            *ppinb |= 0x2;
            delay(750);

            /* turn led off for a slight pause */
            *ppinb |= 0x2;
            delay(100);

        } else if (msg[i]==' ')
        {
            /* leave led off for a long period */
            delay(1000);
        }
    }
}
