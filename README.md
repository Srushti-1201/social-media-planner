# SRUSHTI - Social Media Content Planner

This is a social media content planner application built with Django and React.

## Features
- **Post Management**: Create, edit, and delete social media posts.
- **Scheduling**: Schedule posts for future publication.
- **Analytics Dashboard**: Visualize engagement and post statistics.
- **Multi-Platform Support**: Plan content for Instagram, Facebook, Twitter, LinkedIn, and TikTok.
- **Image Integration**: Fetch images directly from Unsplash.

## Setup
- Python 3.10+
- Node.js 16+
- `pip install -r requirements.txt`
- `npm install --prefix frontend`

## Environment Variables
Copy `.env.example` to `.env` and fill in the values.

- `DATABASE_URL`: The URL of the PostgreSQL database.
- `SECRET_KEY`: A secret key for the Django application.
- `UNSPLASH_ACCESS_KEY`: Your access key for the Unsplash API.

## Local Setup Steps
1. Clone the repository.
2. Install Python dependencies: `pip install -r requirements.txt`
3. Install Node.js dependencies: `npm install --prefix frontend`
4. Copy `.env.example` to `.env` and configure environment variables.
5. Run database migrations: `python manage.py migrate`
6. Build the frontend: `npm run build --prefix frontend`
7. Start the server: `python manage.py runserver`

The application will be available at `http://127.0.0.1:8000/`.

## Database + Migrations Instructions
- For local development, SQLite is used by default.
- For production, PostgreSQL is configured via `DATABASE_URL`.
- To run migrations: `python manage.py migrate`
- To create new migrations: `python manage.py makemigrations`

## How to Run Frontend & Backend Locally
- Backend: `python manage.py runserver`
- Frontend (dev): `npm run dev --prefix frontend`
- Frontend (built): Included in Django server after `npm run build --prefix frontend`

## API Endpoints
- `GET /api/posts/`: Get all posts.
- `POST /api/posts/`: Create a new post.
- `GET /api/posts/{id}/`: Get a single post.
- `PUT /api/posts/{id}/`: Update a post.
- `DELETE /api/posts/{id}/`: Delete a post.
- `GET /api/posts/analytics/`: Get analytics data.
- `GET /api/posts/fetch_image/`: Fetch a random image from Unsplash.
- `GET /api/posts/random_quote/`: Fetch a random quote.

## UI Flow
- `/`: The main page with the list of posts.
- `/posts/new`: The page for creating a new post.
- `/posts/edit/{id}`: The page for editing a post.
- `/dashboard`: The page with the analytics dashboard.

## How to Test
### UI Flow to Test CRUD
1. Open the application at the live URL.
2. **Create**: Click "Create Post", fill the form (title, content, platform, status), submit.
3. **View**: See the new post in the list on the homepage.
4. **Update**: Click "Edit" on a post, modify fields, submit.
5. **Delete**: Click "Delete" on a post, confirm deletion.

### Report/Visualization Page
- Navigate to `/dashboard` to view analytics charts (posts by platform, status, engagement).

### Third-Party API Feature
- In Create/Edit Post form, click "Generate Quote" to fetch a random quote.
- Click "Fetch Image" to get an image from Unsplash (requires API key).

## Deployment
- Deployed on Render.
- PostgreSQL via Supabase.
- The `render.yaml` file in the root of the project defines the deployment configuration.
- Deployment notes: Ensure environment variables are set in Render dashboard.
