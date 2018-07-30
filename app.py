from flask import Flask, render_template, request
import pandas as pd
import jinja2

#define function
##def new_io_table(io_t,factor="no"):

    #Calculate row sum and column sum
    ##c_sum = io_t.sum(axis=0)
    ##r_sum = io_t.sum(axis=1)

    #Append the new row (which is the sum per column)
    ##io_t=io_t.append(c_sum, ignore_index=True)
    #Append the new column (which is the sum per row)
    ##io_t=pd.concat([io_t, r_sum], axis=1, ignore_index=True)
    #Calculate and assign the sum of the whole table to the last cell
    ##io_t.iloc[-1,-1]=sum(io_t)

    ##if(factor != "no"):
        #Connect the factor column to the rest of the table
        ##io_t=pd.concat([io_t, fctr], axis=1)
    ##return(io_t)


app = Flask(__name__)

@app.route('/')
def index():
    # Render the form. Nothing special needs to happen here.
    return render_template('/index.html')


@app.route('/results', methods=['POST'])
def results():
    # Handle form submissions. Can only receive POST requests.
    if request.method == 'POST':
        io_table=pd.read_csv(request.files['io_table'])
        io_t=io_table
        factor=pd.read_csv(request.files['factor'])
        f=factor
        #Calculate row sum and column sum
        c_sum = io_table.sum(axis=0)
        r_sum = io_table.sum(axis=1)

        #Append the new row (which is the sum per column)
        io_table=io_table.append(c_sum, ignore_index=True)
        #Append the new column (which is the sum per row)
        io_table=pd.concat([io_table, r_sum], axis=1, ignore_index=True)
        #Calculate and assign the sum of the whole table to the last cell
        io_table.iloc[-1,-1]=sum(io_table)


        #Connect the factor column to the rest of the table
        io_table=pd.concat([io_table, factor], axis=1)
        io=io_table
        mdl2=pd.DataFrame(io_t.values*f.values, columns=io_t.columns, index=io_t.index)
        mdl1=pd.DataFrame(io_t.values+f.values, columns=io_t.columns, index=io_t.index)
        #option = request.form['model']
        #if option == "mdl1":
            #mdl_t="yes"
            #mdl_t=pd.DataFrame(io_t.values+f.values, columns=io_t.columns, index=io_t.index)
        #elif option == "mdl2":
            #mdl_t=
            #mdl_t=pd.DataFrame(io_t.values*f.values, columns=io_t.columns, index=io_t.index)
        #elif option == "mdl2" and option== "mdl1":
            #mdl1_t=pd.DataFrame(io_t.values+f.values, columns=io_t.columns, index=io_t.index)
            #mdl2_t=pd.DataFrame(io_t.values*f.values, columns=io_t.columns, index=io_t.index) 
        #results = new_io_table(io_table,factor) # Get some results
    return render_template('/results.html', io=io.to_html(), mdl1=mdl1.to_html(),mdl2=mdl2.to_html())
if __name__ == "__main__":
    app.run(debug=True)
