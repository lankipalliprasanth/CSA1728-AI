% Facts: name(Name, DOB)
name(john, '1990-05-15').
name(emma, '1985-11-22').
name(lisa, '2000-02-10').
name(michael, '1978-09-03').

% Query to find the DOB of a person
dob_of(Name, DOB) :-
    name(Name, DOB).

% Query to find all individuals born before a certain date
born_before(Date, Name) :-
    name(Name, DOB),
    DOB @< Date.
