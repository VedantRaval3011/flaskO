
from flask import Flask, jsonify, request
from primary_db import insert_data, get_data

app = Flask(__name__)

# @app.route('/insert', methods=['POST'])
# def insert():
#     data = request.json
#     success = insert_data(data['name'],data['metadata'], data['id'], data['source_location'], data['temporal_frequency'], data['extension'], data['resampling'], data['projections'], data['paused'], data['compression'], data['interleave'])
#     if success:
#         return jsonify({'message': 'Data added successfully'})
#     else:
#         return jsonify({'error': 'Failed to add data'})

@app.route('/view', methods=['GET'])
def get_all():
    data = get_data()
    if data:
        return jsonify({'data':data})
    else:
        return jsonify({'error': 'Failed to get data'})
    
  
# @app.route('/update/<id>', methods=['PUT'])  
# def update_data(id):
#     new_name = request.json.get('name')
#     new_source_location = request.json.get('source_location')
#     new_metadata = request.json.get('metadata')

#     if update(id,new_name,new_source_location,new_metadata):
#         return jsonify({'message':'Data updated successfully'})
#     else:
#         return jsonify({'error':'Failed to update data'})


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    # Container1:
    theme = data.get('theme')
    subtheme = data.get('subtheme')
    base_path = data.get('base_path')
    
    # Container
    extension = data.get('extension')
    compression = data.get('compression')
    sampling = data.get('resampling')
    projection = data.get('projections')


    # Container2: Meta data of th state:
    access_constraints = data.get('access_constraints')
    use_constraints = data.get('use_constraints')
    purpose = data.get('purpose')

    # Container3: Contact info
    contact_person = data.get('contact_person')
    organization = data.get('organization')
    mailing_address = data.get('mailing_address')
    city = data.get('city')
    country = data.get('country')
    contact_telephone = data.get('contact_telephone')
    contact_fax = data.get('contact_fax')
    contact_email = data.get('contact_email')


    # Container4: Geographic location:
    spheroid = data.get('spheroid')
    datum = data.get('datum')


    # Container5: Coverage
    x_ul = data.get('x_ul')
    y_ul = data.get('y_ul')
    x_ur = data.get('x_ur')
    y_ur = data.get('y_ur')
    x_ll = data.get('x_ll')
    y_ll = data.get('y_ll')
    x_lr = data.get('x_lr')
    y_lr = data.get('y_lr')


    # Container6: Metadata stamp
    metadata_stamp_date = data.get('metadata_stamp_date')
    
    # Container7: Citation
    dpb = data.get('dpb')
    osgc = data.get('osgc')
    source_scale = data.get('source_scale')
    source_date = data.get('source_date')
    lineage = data.get('lineage')
    corporate_name = data.get('corporate_name')
    coroporate_address = data.get('corporate_address')


    # Container8: Data Topic Category
    ditc = data.get('ditc')


    # Container9: Language
    language = data.get('language')


    # Container10: Abstract describing data
    dia = data.get('dia')


    # Container11: Data quality
    pd = data.get('pd')
    accReport = data.get('accReport')
    horpor = data.get('horpor')


    metadata = {

        'access_constraints' : access_constraints,
        'use_constraints' : use_constraints,
        'purpose' : purpose,

        'contact_person' : contact_person,
        'organization' : organization,
        'mailing_address' : mailing_address,
        'city' : city,
        'country' : country,
        'contact_telephone' : contact_telephone,
        'contact_fax' : contact_fax,
        'contact_email' : contact_email,

        'spheroid' : spheroid,
        'datum' : datum,

        'x_ul' : x_ul,
        'y_ul' : y_ul,
        'x_ur' : x_ur,
        'y_ur' : y_ur,
        'x_ll' : x_ll,
        'y_ll' : y_ll,
        'x_lr' : x_lr,
        'y_lr' : y_lr,

        'metadata_stamp_date' : metadata_stamp_date,

        'dpb' : dpb,
        'osgc' : osgc,
        'source_scale' : source_scale,
        'source_date' : source_date,
        'lineage' : lineage,
        'corporate_name' : corporate_name,
        'corporate_address' : coroporate_address,

        'ditc' : ditc,
        
        'language' : language,
        
        'dia' : dia,

        'pd' : pd,
        'accReport' : accReport,
        'horpor' : horpor,

    }
    success = insert_data(data['name'],data['metadata'], data['id'], data['source_location'], data['temporal_frequency'], data['extension'], data['resampling'], data['projections'], data['paused'], data['compression'], data['interleave'])
    if success:
        return jsonify({'message': 'Data added successfully'})
    else:
        return jsonify({'error': 'Failed to add data'})


if __name__ == '__main__':
    app.run(debug=True)