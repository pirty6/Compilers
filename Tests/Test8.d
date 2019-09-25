/* Test8: Un programa sencillo con un ciclo y una condicional anidados */

void main() {
  int x = 0;
  while(x < 1) {
    if(x == 1) {
      x = 2;
    } else {
      x = 1;
    }
    while(x > 1) {
      if(x == 2) {
        x = 3;
      }
    }
  }
}
