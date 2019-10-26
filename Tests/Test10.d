/*Un programa sencillo con todas las instrucciones que has definido.*/

enum J = 10;
enum A = "Hola";


void main(string[] args) {
  int a;
  readf("%i", &a);
  bool b = true;
  string c;
  readf("%s", &c);
  if(b  == true) {
    while(a < 1) {
      if(a == 0) {
        a = 1;
      }
      if(a == 1) {
       b = false;
      }
    }
  }
  writeln(c);
}
