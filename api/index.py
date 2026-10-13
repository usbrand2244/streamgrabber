from streamgrabber import StreamGrabber
from flask import jsonify, request

def handler(request):
    # Get IMDb ID from query parameters
    imdb_id = request.args.get('id')
    
    if not imdb_id:
        return jsonify({'error': 'Missing IMDb ID'}), 400
    
    try:
        # Initialize StreamGrabber
        sg = StreamGrabber()
        
        # Get stream links
        result = sg.grab(imdb_id)
        
        return jsonify({
            'success': True,
            'imdb_id': imdb_id,
            'streams': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
