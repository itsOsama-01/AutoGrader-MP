public class Submission4 {
public static void main(String args[]) {
	Submission4 s4 = new Submission4();
	int value = s4.max3(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2]));
	System.out.println(value);
}

int max3(int a, int b, int c) {
  if (a>b && b<c)
    return a;
  else if (b>a && a>c)
    return b;
  else
    return c;
}
}