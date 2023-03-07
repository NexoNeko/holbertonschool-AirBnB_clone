#!/usr/bin/python3
""" Defines the console class """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
import models


class HBNBCommand(cmd.Cmd):
    """ Command shell for hbnb """

    prompt = "(hbnb) "
        
    def emptyline(self):
        """Ignores empty prompts"""
        pass

    def do_EOF(self):
        """Quits CMD at EOF"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, *args):
        """Creates a new instance of a class.
        I.e.: create BaseModel"""
        if args[0] == "":
            print("** class name missing **")
        else:
            try:
                new_model = None
                new_model = eval(f"{args[0]}()")
                print (new_model.id)
                storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, *args):
        """ Prints the string representation of an instance based on
        the class name and id"""
        if args[0] == "":
            print("** class name missing **")
        else:
            #This splits the arguments for further use
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            try:
                all_objs = storage.all()
                obj_class = eval(f"str({args[0]})")
                obj_id = args[1]
                obj = None
                #this is the function that searches
                #for our value and prints it if it finds it.
                key = args[0] + "." + obj_id
                #This part of the code will attempt to
                #get our object.
                try:
                    obj = all_objs.get(f'{key}')
                    if obj == None:
                        print("** no instance found **")
                        return 0
                    print(obj)
                except Exception:
                    print("** no instance found **")
                    return 0
            #Everything under this line is just
            #error handling
            except IndexError:
                print("** instance id missing **")
                return 0
            except NameError:
                print("** class doesn't exist **")
                return 0

    def do_destroy(self, *args):
        """ destroys an instance based on the class name and id"""
        #IF no arguments are giving, assume empty tuple
        if args[0] == "":
            print("** class name missing **")
        else:
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            try:
                #This will try to find out value
                #and set it to obj so we can delete
                all_objs = storage.all()
                obj_class = eval(f"str({args[0]})")
                obj_id = args[1]
                obj = None
            except IndexError:
                print("** instance id missing **")
                return 0
            except NameError:
                print("** class doesn't exist **")
                return 0
            try:
                #This is the part that actually deletes
                #our value after it's setted
                del all_objs[f'{args[0]}.{obj_id}']
                storage.save()
            except KeyError:
                print("** no instance found **")
                return 0


    def do_all(self, *args):
        """ Prints all string representation of all instances based or not on
        the class name.
        Ex: $ all BaseModel or $ all. """
        all_objs = storage.all()
        #IF no arguments are given, just print everything
        if args[0] == "":
            for i in all_objs.keys():
                print(all_objs[i])
        else:
            #If arguments are given, print everything that
            #contains the class name (args[0])
            #TO do this we look up the key names in our
            #dictionary of objects
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            try:
                obj_class = eval(f"str({args[0]})")
                for key, value in all_objs.items():
                    if key.split('.')[0] == args[0]:
                        print(str(value))
            except NameError:
                print("** class doesn't exist **")


    def do_update(self, *args):
        """Updates an instance based on the class name and id by adding or
        updating the attribute"""
        if args[0] == "":
            print("** class name missing **")
        else:
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))

            #missing parameters handler
            if len(args) < 4:
                parametro = ["** instance id missing **", \
                              "** attribute name missing **", \
                              "** value missing **"]
                print(parametro[len(args) - 1])
                return 0

            all_objs = storage.all()
            try:
                obj_class = eval(f"str({args[0]})")
            except NameError:
                print("** class doesn't exist **")
                return 0
            obj_id = args[1]
            obj_attrib = args[2]
            new_value = args[3]
            obj = None
            key = args[0] + "." + obj_id
            #This part of the code will attempt to
            #get our object.
            try:
                obj = all_objs.get(f'{key}')
            except Exception:
                print("** no instance found **")
                return 0
            #This is the part that wil try to update it
            #This eval transforms "string" to string
            #and also floats to floats, etc.
            try:
                obj.__dict__[args[2]] = eval(args[3])
            except AttributeError:
                print("** no instance found **")
                return 0
            except Exception:
                try:
                    #if the eval fails we try just setting
                    #up the value as normal. If this also fails
                    #Then it wasn't a valid instance to begin with
                    obj.__dict__[args[2]] = args[3]
                except Exception:
                    print("** no instance found **")
                    return 0
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
