/* Test17: Usar una variable fuera de su alcance*/

void main() {
  int num1 = 1;
  int num2 = 2;

  if(num1 > num2) {
    int result = nums1;
  } else {
    int result = num2;
  }
  writeln(result);
}
