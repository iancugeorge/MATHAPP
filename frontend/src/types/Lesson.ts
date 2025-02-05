import { ExerciseNode } from "./ExerciseNode.ts";
export interface Lesson {
  id: number;
  name: string;
  description: string;
  code?: string; // if no nested content, you might use this as the exercise entry point
  children?: Lesson[]; // sub-lessons
  exercises?: ExerciseNode[]; // direct exercises for this lesson
}