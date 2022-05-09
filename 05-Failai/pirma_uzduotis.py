import datetime
import os

copied_image_name = "paveiksliukas.jpeg"
new_image_name = "copy.jpeg" 
current_dir = os.getcwd()

date_today = datetime.date.today()

if not os.path.isdir("Datos"):
    os.mkdir("Datos")

with open(copied_image_name, "rb") as failas_read:
    with open(new_image_name, "wb") as failas_write:
        failas_write.writelines(failas_read.readlines())

with open(os.path.join("Datos", f"{date_today}.txt"), "w") as failas:
    failas.write(new_image_name)
