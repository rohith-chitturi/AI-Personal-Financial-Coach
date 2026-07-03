import express, { Application, Request, Response } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import authRoutes from './routes/auth.routes';
import apiRoutes from './routes/api.routes';
import { errorHandler } from './middlewares/error.middleware';

const app: Application = express();

app.use(express.json());
app.use(cors());
app.use(helmet());

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/core', apiRoutes);

// Health check
app.get('/api/health', (req: Request, res: Response) => {
  res.status(200).json({ success: true, message: 'Core Backend API is running' });
});

// Error handling
app.use(errorHandler);

export default app;
