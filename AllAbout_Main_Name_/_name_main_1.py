import AllAbout_Main_Name_.someModule as sm
print(__name__)

sm.method()

if __name__ == "__main__":
    print("This is from main module")
else:
    print("This has been called from some other module")


"""
Here __name__ attribute will be set to __main__ because u r executing this module directly
but we have imported someModule in this module so __name__ attribute of someModule is set to the moduleName.

If __name__ attribute value is set to __main__ it means that this is the entry point.

In the above if we have imported AllAbout_Main_Name_.someModule and the someModule has below code

if __name__ == "__main__":
    print("This is from main module")
else:
    print("This has been called from some other module")
    
so as soon as we imported and called any method of someModule the above if condition is checked and 
corresponding message will be displayed.
"""