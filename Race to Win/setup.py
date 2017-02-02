import cx_Freeze

executables = [cx_Freeze.Executable("RaceToWin.pyw")]

cx_Freeze.setup(
    name = "Race To Win!",
    options = {"build_exe":{"packages":["pygame"],"include_files":["background.jpg","crash.ogg","freesansbold.ttf","greenCar.png","icon.png","intro.jpg","racecar.png","soundtrack.ogg","yellowCar.png"]}},
    executables = executables
    
    )
