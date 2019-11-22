/*
 * CS122A_Project.c
 *
 * Created: 11/20/2019 3:22:11 PM
 * Author : Administrator
 */ 

#include <avr/io.h>
#include <avr/delay.h>


int main(void)
{
    DDRA = 0x00; PORTA = 0x00;
    DDRB = 0xFF; PORTB = 0x00;
    DDRC = 0xFF; PORTC = 0x00;
    DDRD = 0xFF; PORTD = 0x00;
    while (1) 
    {
        if( ~PINA & (1 << PINA0) ){
            PORTB = 0x01;
        }else if( ~PINA & (1 << PINA1) ){
            PORTB = (1 << PINB1);    
        }else {
            PORTB = 0x03;
        }            
        //_delay_ms(2);
        //PORTB = 0x00;
       // _delay_ms(3);
    }
}

