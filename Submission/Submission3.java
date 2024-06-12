public class Submission3 {
public static void main(String args[]) {
	Submission3 s3 = new Submission3();
	int value = s3.max3(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2]));
	System.out.println(value);
}

int max3(int a, int b, int c) {
  if (a>b && a>c)
    return a;
  else if (b>a && b>c)
    return b;
  else
   return c;
}
}