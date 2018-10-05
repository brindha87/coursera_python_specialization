# Write code using find() and string slicing to extract the number at the end of the line below.
# text = "X-DSPAM-Confidence:    0.8475";
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

colon_pos = text.find(':')
str_val = text[colon_pos+1 : ]
str_val_nospaces = str_val.lstrip()
val = float(str_val_nospaces)

print ("Extracted value", val)
