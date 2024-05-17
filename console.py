import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program when End of File (EOF) is reached"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

  
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        
        try:
            # Dynamically fetch the class from the models module
            cls = getattr(sys.modules[__name__], arg)
            if issubclass(cls, BaseModel):
                instance =cls()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        except AttributeError:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]

        # Retrieve the class dictionary from storage
        classes = storage.all().keys()

        if class_name not in classes:
            print("** class doesn't exist **")
            return
        
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"

        if key not in storage.all():
            print("** no instance found **")
            return
        
        print(storage.all()[key])



    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
