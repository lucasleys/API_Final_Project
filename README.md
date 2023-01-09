# API_Final_Project
## Inhoud
- [Uitleg](#uitleg)
- [API](#api)
- [Uitbreiding](#uitbreiding)
- [Links](#links)
- [Postman Screenshots](#Postman-screenshots)
- [API docs Screenshots](#API-docs-screenshots)
- [Auteur](#author)
## Uitleg
 Het thema van mijn api is eigenlijk colruyt, maar .i.p.v. klant gericht te zijn, is het nu beheerder gericht. Dus er zit wel nog wat in van mijn vorig project. Aangezien ik daar ook jobstudent ben en redelijk veel weet over dit onderwerp, was de keuze snel gemaakt.

## API
Mijn api is hier te vinden:  
Link: https://system-service-lucasleys.cloud.okteto.net/  

## Uitbreiding
### 2.1 Pytest testen voor GET Endpoints
#### Testen voor alle users te tonen
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Get Users](images/Test_Code_Get_Users.png)
- Resultaat
![Image Test Result Get Users](images/Test_Result_Get_Users.png)
#### Testen voor actieve user te tonen
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Get Active User](images/Test_Code_Get_Active_User.png)
- Resultaat
![Image Test Result Get Active User](images/Test_Result_Get_Active_User.png)
#### Testen voor alle producten te tonen
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Get Products](images/Test_Code_Get_Products.png)
- Resultaat
![Image Test Result Get Products](images/Test_Result_Get_Products.png)
#### Testen voor alle locaties te tonen
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Get Locations](images/Test_Code_Get_Locations.png)
- Resultaat
![Image Test Result Get Locations](images/Test_Result_Get_Locations.png)
#### 2.1.1 Test alle niet-GET endpoints
##### POST Testen
###### Testen om een user aan te maken
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Create User](images/Test_Code_Create_User.png)
- Resultaat
![Image Test Result Create User](images/Test_Result_Create_User.png)
###### Testen om een product aan te maken
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Create Product](images/Test_Code_Create_Product.png)
- Resultaat
![Image Test Result Create Product](images/Test_Result_Create_Product.png)
###### Testen om een locatie aan te maken
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Create Location](images/Test_Code_Create_Location.png)
- Resultaat
![Image Test Result Create Location](images/Test_Result_Create_Location.png)
##### PUT Testen
###### Testen om een product te updaten
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Update Product](images/Test_Code_Update_Product.png)
- Resultaat
![Image Test Result Update Product](images/Test_Result_Update_Product.png)
##### DELETE Testen
###### Testen om een product te verwijderen
- Hier kan u zien hoe de test ineen zit.   
![Image Test Code Delete Product](images/Test_Code_Delete_Product.png)
- Resultaat
![Image Test Result Delete Product](images/Test_Result_Delete_Product.png)

## Links

[Link github repo](https://github.com/lucasleys/API_Final_Project.git)   
[Gehoste API link](https://system-service-lucasleys.cloud.okteto.net/) 

## Postman screenshots

### POST /token
Om een token te kunnen koppelen aan de user zodat die toegang heeft tot de endpoints geef ik password en username mee. 
![Image postman /token](/images/Postman_Post_Token.png)  

### GET Users
Deze endpoint zorgt ervoor dat u alle gebruikers te zien krijgt. 
![Image postman Get Users](/images/Postman_Get_Users.png) 

### GET Current User
Deze endpoint zorgt ervoor dat u de huidige gebruiker te zien krijgt. 
![Image postman Get Active User](/images/Postman_Get_Active_User.png) 

### POST User
Doormiddel van deze endpoint kunt u een gebruiker aanmaken door de username en password mee te geven. 
![Image postman Post User](/images/Postman_Post_User.png)

### GET Products
Deze endpoint zorgt ervoor dat u alle producten te zien krijgt. 
![Image postman Get Products](/images/Postman_Get_Products.png) 

### POST Product
Doormiddel van deze endpoint kunt u een product aanmaken door de naam, prijs en categorie mee te geven. 
![Image postman Post Product](/images/Postman_Post_Product.png) 

### PUT Product
Doormiddel van deze endpoint kunt u een bestaand product aanpassen door de naam in de path op te geven en dan de gegevens die je wilt aanpassen meegeven. 
![Image postman Put Product](/images/Postman_Put_Product.png)

### DELETE Product
Doormiddel van deze endpoint kunt u een bestaand product verwijderen door de product_id mee te geven. 
![Image postman Delete Product](/images/Postman_Delete_Product.png)

### GET Locations
Deze endpoint zorgt ervoor dat u alle locaties te zien krijgt.  
![Image postman Get Locations](/images/Postman_Get_Locations.png)

### POST Location
Doormiddel van deze endpoint kunt u een locatie aanmaken door de stad, postcode en gerant/chef mee te geven. 
![Image postman Post Location](/images/Postman_Post_Location.png)

## API docs screenshots

## Author
Lucas Leys 
[email](mailto:r0881339@student.thomasmore.be)  