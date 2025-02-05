export interface Exercise {
    id: number;
    topic_id: number;
    type: string;
    difficulty: number;
    question: string;
    solution: number;
    hints: string[];
    steps?: string[]; // Optional, if provided by the backend
  }
  