def app(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
	return[bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding="utf-8")]
#	query = urlparse.urlparse(environ['QUERY_STRING'])[4]
#	query_items = query.split("&")
#	status = '200 OK'
#	response_headers = [
#		('Content-type', 'text/plain')
#	]
#	body = ''
#	for i in query_items:
#		body += i + '\r\n'
#	start_response(status, response_headers)
#	return [body]
