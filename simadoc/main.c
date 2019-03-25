/* Created by Douglas Sandy, ASU
 */

#include "_hw5/led.h"
#include "_hw5/uart.h"
#include "_hw5/delay.h"
#include "temp.h"

int main(void)
{
    /* initialize hardware */
    uart_init();
    led_init();
    temp_init();

    uart_writestr("SER 486 HW5 - Doug Sandy\n\r");
    temp_start();
    while(1) {
        if (led_ison()) {
            led_off();
        } else {
            led_on();
        }

        delay(10);
        if (temp_is_data_ready())
        {
            int data = temp_get();
            temp_start();
            uart_writedec32(data);
            uart_writestr("   \r");
        }
    }
    return 0;
}
