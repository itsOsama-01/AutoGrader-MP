public class Submission2 {
public static void main(String args[]) {
	Submission2 s2 = new Submission2();
	int value = s2.max3(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2]));
	System.out.println(value);
}
int max3(int a, int b, int c) {
if (a>b)
  if (a>c)
    return a;
  else
    return c;
else
  if (b>c)
    return b;
  else
    return c;
}
}