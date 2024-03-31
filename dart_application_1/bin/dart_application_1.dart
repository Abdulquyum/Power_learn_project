import 'package:dart_application_1/dart_application_1.dart' as dart_application_1;

/*void main(List<String> arguments) {
  print('Hello world: ${dart_application_1.calculate()}!');
}*/
void main()
{
    int number;
    number = stdin.readLineSync!();

    if (number > 10)
    {
        print("Your number is greater than 10");
    }
    else if (number < 10)
    {
        print("Your number is less than 10");
    }
    else {
        print("Your number is equal to 10");
    }
}