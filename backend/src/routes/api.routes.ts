import { Router, Request, Response } from 'express';
import { protect } from '../middlewares/auth.middleware';

const router = Router();

// Apply auth middleware to all API routes
router.use(protect);

// Transactions placeholder
router.get('/transactions', (req: Request, res: Response) => {
  res.json({ success: true, message: 'Get all transactions - Not implemented' });
});

router.post('/transactions', (req: Request, res: Response) => {
  res.json({ success: true, message: 'Create transaction - Not implemented' });
});

// Budgets placeholder
router.get('/budgets', (req: Request, res: Response) => {
  res.json({ success: true, message: 'Get all budgets - Not implemented' });
});

router.post('/budgets', (req: Request, res: Response) => {
  res.json({ success: true, message: 'Create budget - Not implemented' });
});

// Goals placeholder
router.get('/goals', (req: Request, res: Response) => {
  res.json({ success: true, message: 'Get all goals - Not implemented' });
});

router.post('/goals', (req: Request, res: Response) => {
  res.json({ success: true, message: 'Create goal - Not implemented' });
});

export default router;
