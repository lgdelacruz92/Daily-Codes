#include <studio.h>

int main(void)
{
    int userAge;
    int insurancePrice;

    printf("Enter your age: ");
    scanf("%d", &userAge);

    if (userAge < 16)
    { // Age 15 and under
        printf("Too young.\n");
        insurancePrice = 0;
    }
    else if (userAge < 25)
    { // Age 16 - 24
        insurancePrice = 4800;
    }
    else if (userAge < 40)
    { // Age 25 - 39
        insurancePrice = 2350;
    }
    else
    { // Age 40 and up
        insurancePrice = 2100;
    }

    printf("Annual price: $%d\n", insurancePrice);
    return 0;
}