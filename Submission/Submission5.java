public class Submission5 {
public static void main(String args[]) {
	Submission5 s5 = new Submission5();
	int value = s5.max3(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2]));
	System.out.println(value);
}

int max3(int a, int b, int c) {
  if (a>b && b>c)
    return a;
  else if (b>c)
    return b;
  else
    return c;
}
}