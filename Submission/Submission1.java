public class Submission1 {
public static void main(String args[]) {
	Submission1 s1 = new Submission1();
	int value = s1.max3(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2]));
	System.out.println(value);
}

int max3(int a, int b, int c) {
  if (a>=b)
    if (a>=c)
      return a;
    else
      return c;
  else
    if (b>=c)
      return b;
    else
      return c;
}
}