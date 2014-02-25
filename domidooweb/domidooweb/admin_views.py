from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config
import uuid
import os.path

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Place,
    )

def save_uploaded_file(form_field, upload_dir):
        input_file = form_field.file
        original_filename = form_field.filename
        dir(input_file)
        the_name = "%s.%s" %( uuid.uuid4(), os.path.basename(original_filename) )
        file_path = os.path.join(upload_dir, the_name)

        temp_file_path = file_path + '~'

        output_file = open(temp_file_path, 'wb')
        # Finally write the data to a temporary file
        input_file.seek(0)
        while True:
            data = input_file.read(2<<16)
            if not data:
                break
            output_file.write(data)

        output_file.close()

        os.rename(temp_file_path, file_path)

        return the_name







@view_config(route_name='admin.home', renderer='admin/home.mak')
def admin_home(request):
    return {}


@view_config(route_name='admin.places.new', renderer='admin/places_new.mak')
def place_new(request):
    if(request.method == 'GET'):
        return {'error': '', 'name': '', 'city': ''}
    else:
        dat = request.POST
        name = dat.get('name')
        city = dat.get('city')
        image = dat.get('image')

        upload_dir = request.registry.settings['images.uploaded']
        if hasattr(image, 'filename'):
            image_filename = save_uploaded_file(request.POST['image'], upload_dir)
        else:
            image_filename = None

        place = Place(name=name, city=city, image=image_filename)
        DBSession.add(place)

        return HTTPFound(location = request.route_url('home'))
