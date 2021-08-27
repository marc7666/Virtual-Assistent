lynt:
	pylint bot.py
	pylint colors.py
	pylint sightseeing.py
	pylint town_hall.py
	pylint barcelona_file.py
	pylint girona_file.py
	pylint internet_payment.py
	pylint lleida_file.py
	pylint phone_payment.py
	pylint tarragona_file.py
	pylint dgt_fine.py
	pylint dgt_allegation.py
	pylint complaint_ord.py
	pylint undeclared_tickets.py
	pylint software_complaint.py
	pylint cash_payments.py
	pylint e_commerce.py
	pylint property_rental.py
	pylint address_and_tels.py

play:
	python3 bot.py


all:
	make lynt
	make play
