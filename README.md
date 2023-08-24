# InventoryManagement_Console

An Event Equipment Rental shop needs to maintain information about the
available equipment. The shop rents out the equipment to the customers for a fee
which is charged on a 5-day basis. If any party fails to return the rented equipment
within 5 days, a fine is charged on a per-day basis.
The shop maintains information about the available equipment in a text file. An
application needs to be developed which will read the text file and display all the
equipment available. Then with each transaction, a note/invoice should be
generated for the particular customer and should be written to a file along with the
details of the equipment involved in the transaction. The stock of the equipment
should also be updated after each transaction. For example, if the store had 14 table
cloths, and if one table cloth is rented by a customer then the number (stock) should
be changed to 13. In the case of returning said equipment, a note/invoice should
again be generated for the customer returning the equipment. The stock should also
be updated i.e. the quantity of the equipment returned should be increased by 1 as
well.
A sample format of the text file containing the information about the equipments
are as follows:
Velvet Table Cloth, Saathi, $8, 20
Microphone Set, Audio Technica, $189, 15
Disco Light Set, Sonoff, $322, 24
7.1 Surround Sound Speaker Set, Dolby, $489,4
Dinner Table 8x5, Panda Furnitures, $344, 8
*1st column contains the name of the equipment, 2

nd column contains name of brand,

3
rd column contains the price for rent (5 days), 4

th column contains the quantity

available
**You can use your own format and add other information too
A note/invoice should be generated for each transaction. When a customer
rents equipment, a note/invoice should be generated which must contain the name
of the equipment, name of brand, name of the customer, date and time of rental and
the total amount to be paid for the equipment. If a customer decides to rent more
than one piece of equipment, then the amount should be added up for all the
equipment rented.
When a customer returns an equipment, a note/invoice should be generated
again which should contain the name of the customer, name of the equipment, name
of brand, date and time of return. The duration of the equipment rental should be set
to 5 days, and if a customer is late for returning the equipment, a fine should be
applied on a daily basis which should be written to the file again.
* The format of the notes/invoices is up to you. But each file should have a unique
name.
