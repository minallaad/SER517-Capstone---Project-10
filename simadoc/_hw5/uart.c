/********************************************************
 * uart.c
 *
 * this file provides function implementation for SER486
 * uart library functions.
 *
 * Author:   Doug Sandy
 * Date:     2/16/2018
 * Revision: 1.0
 *
 * Copyright(C) 2018, Arizona State University
 * All rights reserved
 *
 */#include <avr/interrupt.h>
#include "serial.h"
#include "simulavr_info.h"
SIMINFO_DEVICE("atmega328");
SIMINFO_CPUFREQUENCY(F_CPU);
SIMINFO_SERIAL_IN("D0", "-", 9600);
SIMINFO_SERIAL_OUT("D1", "-", 9600);

/* intialize the atmega UART */
void uart_init() {
    serial_init();
    sei();
}

/* send one character to the atmega UART */
void uart_writechar(char data)
{
    serial_writechar((uint8_t)data);
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
void uart_writestr(char * str)
{
    unsigned int i;

    /* loop for each character in the string */
    for (i=0; str[i]!=0;i++) {
        /* output the character to the UART */
        uart_writechar(str[i]);
    }
}


void uart_writehex8(unsigned char num)
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

void uart_writehex16(unsigned int num)
{
    signed char i;
    unsigned char ch;
    /* loop for each byte in the word */
    for (i=8;i>=0;i-=8) {
        /* extract a single nibble */
        ch = (unsigned char)((num>>i)&0xff);
        /* convert to ascii hex digit */
        uart_writehex8(ch);
    }
}

void uart_writedec32(int num)
/* output the decimal representation of a byte to the console
 * leading zeros are not displayed */
{
    int neg = 0;
    int i,pow;
    char digit[5];

    if (num<0) {
        num *= -1;
        neg = 1;
    }

    pow = 1;
    for (i=0;i<5;i++) {
        digit[i] = (num%(pow*10))/(pow);
        num -= digit[i];
        pow*=10;
    }

    if (neg) {
        uart_writechar('-');
    } else {
        uart_writechar(' ');
    }

    int leading = 0;
    for (i=4;i>=0;i--)
    {
        if ((digit[i])||(leading)||(i==0))
        {
            uart_writechar(digit[i]+'0');
            leading =1;
        }
    }
}
