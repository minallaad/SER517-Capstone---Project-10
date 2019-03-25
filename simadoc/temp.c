/********************************************************
 * temp.h
 *
 * this file provides function implementation for SER486
 * temp (temperature sensor) library code code.
 *
 * Author:   Doug Sandy
 * Date:     2/16/2018
 * Revision: 1.0
 *
 * Copyright(C) 2018, Arizona State University
 * All rights reserved
 *
 */

#define PRR    (*((volatile unsigned char *)0x64))
#define ADCL   (*((volatile unsigned char *)0x78))
#define ADCH   (*((volatile unsigned char *)0x79))
#define ADCSRA (*((volatile unsigned char *)0x7A))
#define ADCSRB (*((volatile unsigned char *)0x7B))
#define ADMUX  (*((volatile unsigned char *)0x7C))
#define DIDR0  (*((volatile unsigned char *)0x7E))
#define DDRB   (*((volatile unsigned char *)0x24))

/* initialize the ADC channel and reference voltage */
 void temp_init()
 {
     ADMUX = 0x00;
     ADCSRA = 0x86;
 }

 /* determine if the ADC conversion has completed */
 int temp_is_data_ready()
 {
    return (ADCSRA&0x40)?0:1;
 }

 /* start the ADC conversion */
 void temp_start()
 {
     ADCSRA |= 0x40;
 }

 /* return the value of the temperature sensor measured in degrees celsius */
 int temp_get()
 {
     unsigned char lo = ADCL;
     unsigned char hi = ADCH;
     long temp = ((unsigned long)(hi<<8)) | (unsigned long)lo;
     //temp = (temp*101)/100 - 273;
     return temp;
 }

