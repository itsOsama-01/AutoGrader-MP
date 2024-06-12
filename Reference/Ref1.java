public class Ref1 {
public static void main(String args[]) {
	Ref1 r = new Ref1();
	int value = r.max3(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2]));
	System.out.println(value);
}
int max3(int a, int b, int c) {
  if (a>=b && a>=c)
    return a;
  else if (b>=a && b>=c)
    return b;
  else
    return c;
}
}