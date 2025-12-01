#include <stdio.h>
#include <string.h>
#include <ctype.h>

void decryptPassword(char password[]);

int main()
{
    /* 所有变量声明必须在函数开头 */
    char password[100];
    int length;
    
    printf("请输入密码：");
    fgets(password, sizeof(password), stdin);
    
    /* 去掉换行符 */
    length = strlen(password);
    if (length > 0 && password[length - 1] == '\n')
        password[length - 1] = '\0';
    
    printf("密码：%s\n", password);
    
    decryptPassword(password);
    
    printf("原文：%s\n", password);
    
    return 0;
}

void decryptPassword(char password[])
{
    /* 所有变量声明必须在函数开头 */
    int i;
    char ch;
    
    for (i = 0; password[i] != '\0'; i++)
    {
        ch = password[i];
        
        if (isupper(ch))  /* 大写字母 */
        {
            password[i] = 'A' + ('Z' - ch);
        }
        else if (islower(ch))  /* 小写字母 */
        {
            password[i] = 'a' + ('z' - ch);
        }
        /* 非字母字符不变 */
    }
}