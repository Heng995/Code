public class pointCircle{
    public static void main(String[] args){
        circle c1 = new circle();
        circle c2 = new circle(new Point(1,2),5);
        circle c3 = new circle(10);
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
        extracted();
    }

    private static void extracted() {
        circle.totalCircle();
    }
}
class Point{ //原點座標
    int x,y;
    Point(int x, int y) {this.x=x;this.y=y;}
}
class circle{
    Point p; //原點座標
    double r;
    static int total=0;
    {total++;}
    circle(){
        p = new Point(0,0);
        r = 0;
    }
    circle(Point p, double r){
        this.p=p;
        this.r=r;
    }
    circle(double r){
        p = new Point(0,0);
        this.r = r;
    }
    public String toString(){
        return "圓心座標="+p.x+","+p.y+"  半徑="+r+"  面積="+r*r*3.14;
    }
    double calArea(){
        return r*r*3.14;
    }
    static void totalCircle(){
        System.out.println("總共"+total+"圈h");
    }
}