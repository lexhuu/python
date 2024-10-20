#include<stdio.h>
void main()
{
    int a[10],top=-1,option,item,i,n;
    do
    {
        printf("\n enter your option");
        print("\nstack operations\n1.push\n2.pop\n3" display\n4.exit\n");
        scanf("%d",&option);
        switch(option)
        {
            case1:if(top==9)
            printf("stack is full")
            else
            printf("enter the element to be pushed");
            scanf("%d",&a[top]);
            top=top+1;
            a[top]=item;
            break;
            case2:if(top<0)
            printf("stack empty");
            else
            item=a[top];
            top--;
            printf("the elements%ddetected",item);
            break;
            case3:
            printf("stack elements are\n");
            for(i=0;i<top;i++)
            printf("%d\n",a[i]);
            break;
            }
            }
            while(option!=4);
            }


        

    
