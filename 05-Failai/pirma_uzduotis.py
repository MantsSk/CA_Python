import datetime

image_name = "copy" 

with open("paveiksliukas.jpeg", "rb") as failas_read:
    with open(f"/Users/mantasskara/Desktop/{image_name}.jpeg", "wb") as failas_write:
        failas_write.writelines(failas_read.readlines())

with open(f"{datetime.date.today()}.txt", "w") as failas:
    failas.write(image_name)
