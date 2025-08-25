# ✅ Deployment Checklist

## 🎯 Quick Start (5 minutes)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - ShipTrack Pro"
# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 2. Deploy Backend (Railway)
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables:
   - `ENVIRONMENT=production`
   - `FRONTEND_URL=https://your-app-name.vercel.app` (update after step 3)

### 3. Deploy Frontend (Vercel)
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. "New Project" → Import your GitHub repo
4. Configure:
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. Environment Variables:
   - `VITE_API_URL=https://your-backend-url.railway.app`

### 4. Update CORS
1. Get your Vercel URL
2. Update Railway environment variable:
   - `FRONTEND_URL=https://your-actual-vercel-url.vercel.app`

## 🧪 Test Your Deployment

### Login Credentials:
- **Admin**: `admin` / `admin123`
- **Manager**: `manager` / `manager123`
- **Employee**: `employee` / `employee123`
- **Customer**: `testuser` / `password123`

### URLs to Test:
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-app.railway.app/docs`
- Health Check: `https://your-app.railway.app/docs`

## 🎉 You're Live!

Your ShipTrack Pro application is now deployed and accessible worldwide!

## 💰 Cost: $0/month

Both services offer generous free tiers perfect for this application.

## 🔧 Troubleshooting

**CORS Issues**: Ensure FRONTEND_URL matches your Vercel domain exactly
**Build Failures**: Check logs in Railway/Vercel dashboards
**Database**: Currently using SQLite (works for demo, consider PostgreSQL for production)
