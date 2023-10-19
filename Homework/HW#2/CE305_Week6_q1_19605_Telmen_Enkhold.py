def crc_encode(data, polynomial):
    # Append zeros for division
    data += '0' * (len(polynomial) - 1)
    data_bits = list(data)
    polynomial_bits = list(polynomial)

    for i in range(len(data) - len(polynomial) + 1):
        if data_bits[i] == '1':
            for j in range(len(polynomial)):
                data_bits[i + j] = '0' if data_bits[i + j] == polynomial_bits[j] else '1'

    return data[:-len(polynomial) + 1] + ''.join(data_bits[-len(polynomial) + 1:])


def crc_decode(received_data, polynomial):
    received_data = received_data.replace(" ", "")  # Remove spaces
    received_bits = list(received_data)
    polynomial_bits = list(polynomial)

    for i in range(len(received_data) - len(polynomial) + 1):
        if received_bits[i] == '1':
            for j in range(len(polynomial)):
                received_bits[i + j] = '0' if received_bits[i + j] == polynomial_bits[j] else '1'

    if '1' in ''.join(received_bits[-len(polynomial) + 1:]):
        return 'Error'
    else:
        return 'No error'


# Test cases
org_sig1 = '1010'
poly = '100101'
encoded_sig1 = crc_encode(org_sig1, poly)
print(f"Encoded: {org_sig1} => {encoded_sig1}")

received_sig1 = '1010 00111'
result1 = crc_decode(received_sig1, poly)
print(f"Decoding result for {received_sig1}: {result1}")

org_sig2 = '1100'
encoded_sig2 = crc_encode(org_sig2, poly)
print(f"Encoded: {org_sig2} => {encoded_sig2}")

received_sig2 = '1010 01111'
result2 = crc_decode(received_sig2, poly)
print(f"Decoding result for {received_sig2}: {result2}")

received_sig3 = '1100 11001'
result3 = crc_decode(received_sig3, poly)
print(f"Decoding result for {received_sig3}: {result3}")

received_sig4 = '1100 11111'
result4 = crc_decode(received_sig4, poly)
print(f"Decoding result for {received_sig4}: {result4}")
