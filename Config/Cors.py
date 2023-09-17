from fastapi.middleware.cors import CORSMiddleware


def init_cors(app):
	origins = [
		# "http://localhost",
	]
	origin = origins if len(origins) > 0 else ["*"]
	return app.add_middleware(
		CORSMiddleware,
		allow_origins=origin,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)