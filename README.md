<!DOCTYPE html>
<html>
<head>
<!--     <title>Cross-Broker Script Mapping</title> -->
</head>
<body>

<h1>Cross-Broker Script Mapping</h1>

<h2>Project Overview</h2>
<p>The goal of this project is to create a singular mapping of the script master data for 5 brokers. This allows users to select a trading script from any broker and get the corresponding mapping for the other 4 brokers. This cross-broker mapping is important for aligning script symbols across different trading platforms.</p>

<h2>Steps Followed:</h2>

<h3>1. Data Loading</h3>
<p>We started by loading the script master data from various brokers. The data for each broker was provided in CSV files. For this project, we are focusing on 5 brokers: ICICI, Zerodha, Fyers, and two others yet to be added because of large size.</p>

<h3>2. Data Inspection</h3>
<p>For each broker's data, we inspected the columns and the data structure to understand how to standardize the fields across brokers.</p>

<p>For example:</p>
<ul>
    <li>ICICI's data had columns like <code>SC</code>, <code>ISIN</code>, <code>EC</code>, and <code>SG</code>, which we renamed to standard terms such as <code>tradingsymbol</code>, <code>ISIN</code>, <code>exchange</code>, and <code>segment</code>.</li>
    <li>Zerodha's data had columns for <code>tradingsymbol</code>, <code>exchange</code>, and <code>segment</code>.</li>
    <li>Fyers' data was provided with columns like <code>Instrument_Name</code> and <code>ISIN_Code</code>, and we renamed them to <code>tradingsymbol</code> and <code>ISIN</code> to match the format of the other brokers' data.</li>
</ul>

<h3>3. Data Cleaning</h3>
<p>We selected the relevant columns for each broker's data and cleaned them to ensure consistency across all datasets. The primary fields used for merging the data were:</p>
<ul>
    <li><code>tradingsymbol</code>: The script symbol used for trading.</li>
    <li><code>ISIN</code>: International Securities Identification Number, which is unique for each stock.</li>
</ul>

<h3>4. Merging Data</h3>
<p>We performed an outer join to merge the data from different brokers based on the <code>tradingsymbol</code> and <code>ISIN</code>. This ensures that we have a consolidated view where the script from one broker is mapped to the other brokers.</p>

<p>Example of merging ICICI and Zerodha data:</p>
<pre>
<code>merged_df = pd.merge(icici_cleaned, zerodha_cleaned, on=['tradingsymbol', 'exchange'], how='outer', suffixes=('_icici', '_zerodha'))</code>
</pre>

<h3>5. Handling Additional Brokers</h3>
<p>We applied the same process to the Fyers data, cleaning it and merging it with the ICICI + Zerodha combined dataset. The same steps will be repeated for the remaining two brokers.</p>

<h3>6. Final Output</h3>
<p>After merging the data from all 3 brokers, we will have a complete mapping available in a singular CSV file (<code>singular_script_mapping.csv</code>). This file will allow users to select a trading symbol from any broker and get the equivalent symbols from the other 4 brokers.</p>

</body>
</html>
