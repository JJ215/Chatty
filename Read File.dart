import 'dart:io';

main() async {
  WriteFile();
}

dynamic ReadFile() async {
  var file = File('data-copy.txt');
  var contents;
  contents = await file.readAsString();
  print(contents);
}

dynamic WriteFile() async {
  {
    // Write file
    var fileContents = "Jaylen Hampton";
    var fileCopy = await File('data-copy.txt').writeAsString(fileContents);
    print(await fileCopy.exists());
    print(await fileCopy.length());
  }
}
