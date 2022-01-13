public class Test2 {
    static int c = 100;
    public static void main(String[]args){
        System.out.println("Hello主程式");
        B obj3 = new B();
        A obj1 = new A();
    }
    static{System.out.println("主類別初始區塊");}
    {System.out.println("主類別non-static");}
}

class A{
    static{System.out.println("A 初始區塊");}
    {System.out.println("A non-static 初始區塊");}
}
class B{
    static{System.out.println("B 初始區塊");}
    {System.out.println("B non-static 初始區塊");}
}