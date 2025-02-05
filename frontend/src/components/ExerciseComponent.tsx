// src/components/ExerciseComponent.tsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AlertCircle, CheckCircle2, HelpCircle, Timer, Trophy, ChevronDown } from 'lucide-react';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';
import axios from 'axios';
import { InlineMath } from 'react-katex';
import 'katex/dist/katex.min.css';

// Define prop type for ExerciseComponent
interface ExerciseComponentProps {
  lessonCode: string;
}

// Generate array of difficulty levels 1-14
const DIFFICULTY_LEVELS = Array.from({ length: 14 }, (_, i) => i + 1);

const ExerciseComponent: React.FC<ExerciseComponentProps> = ({ lessonCode }) => {
  const [exercise, setExercise] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [userAnswer, setUserAnswer] = useState<string>('');
  const [feedback, setFeedback] = useState<{ type: string; message: string }>({ type: '', message: '' });
  const [showHints, setShowHints] = useState<boolean>(false);
  const [timer, setTimer] = useState<number>(0);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [attempts, setAttempts] = useState<number>(0);
  const [score, setScore] = useState<number>(0);
  const [difficulty, setDifficulty] = useState<number>(1); // Default to middle difficulty

  useEffect(() => {
    fetchExercise();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [difficulty, lessonCode]);

  useEffect(() => {
    let intervalId: NodeJS.Timeout;
    if (isRunning) {
      intervalId = setInterval(() => {
        setTimer(prev => prev + 1);
      }, 1000);
    }
    return () => clearInterval(intervalId);
  }, [isRunning]);

  const fetchExercise = async () => {
    setLoading(true);
    setError(null);
    setFeedback({ type: '', message: '' });
    setUserAnswer('');
    setShowHints(false);
    setTimer(0);
    setAttempts(0);
    setIsRunning(true);

    try {
      // Use the lessonCode prop in the endpoint URL.
      const response = await axios.get(`http://localhost:8000/exercises/${lessonCode}`, {
        params: { 
          difficulty: difficulty 
        }
      });
      setExercise(response.data);
    } catch (err) {
      setError('Failed to load exercise. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const navigate = useNavigate();

  useEffect(() => {
    if (error) {
      // Redirecționează după 3 secunde
      const timer = setTimeout(() => {
        navigate('/lessons');
      }, 0);
      return () => clearTimeout(timer);
    }
  }, [error, navigate]);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setAttempts(prev => prev + 1);

    if (!exercise) return;

    if (userAnswer.trim() === exercise.solution) {
      setFeedback({
        type: 'success',
        message: 'Correct! Well done!'
      });
      setScore(prev => prev + Math.max(10 - attempts, 1));
      setIsRunning(false);
    } else {
      setFeedback({
        type: 'error',
        message: 'Not quite right. Try again!'
      });
    }
  };

  const formatTime = (seconds: number): string => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const getDifficultyColor = (level: number) => {
    if (level <= 4) return 'bg-green-100 text-green-800';
    if (level <= 9) return 'bg-yellow-100 text-yellow-800';
    return 'bg-red-100 text-red-800';
  };

  if (loading) {
    return (
      <Card className="w-full max-w-2xl mx-auto">
        <CardContent className="p-6">
          <div className="space-y-4">
            <div className="h-4 bg-gray-200 rounded animate-pulse" />
            <div className="h-8 bg-gray-200 rounded animate-pulse" />
            <div className="h-12 bg-gray-200 rounded animate-pulse" />
          </div>
        </CardContent>
      </Card>
    );
  }

  if (error) {
    return (
      <Alert variant="destructive" className="max-w-2xl mx-auto">
        <AlertCircle className="h-4 w-4" />
        <AlertDescription>{error}</AlertDescription>
      </Alert>
    );
  }

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader>
        <div className="flex justify-between items-center">
          <CardTitle>Math Exercise</CardTitle>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2">
              <Trophy className="h-4 w-4" />
              <span>{score} pts</span>
            </div>
            <div className="flex items-center gap-2">
              <Timer className="h-4 w-4" />
              <span>{formatTime(timer)}</span>
            </div>
          </div>
        </div>
      </CardHeader>

      <CardContent className="space-y-6">
        <div className="flex justify-between items-center">
          <span className={`px-2 py-1 rounded text-sm ${getDifficultyColor(difficulty)}`}>
            Level {difficulty}
          </span>
          <select
            value={difficulty}
            onChange={(e) => setDifficulty(Number(e.target.value))}
            className="text-sm border rounded p-1"
          >
            {DIFFICULTY_LEVELS.map(level => (
              <option key={level} value={level}>
                Level {level}
              </option>
            ))}
          </select>
        </div>

        <div className="p-4 bg-gray-50 rounded-lg">
          <InlineMath math={exercise.questionLatex} />
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="answer" className="block text-sm font-medium mb-2">
              Your Answer:
            </label>
            <Input
              type="text"
              id="answer"
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              placeholder="Enter your answer here"
              className="w-full"
            />
          </div>

          <Button type="submit" className="w-full">
            Submit Answer
          </Button>
        </form>

        {feedback.message && (
          <Alert variant={feedback.type === 'success' ? 'default' : 'destructive'}>
            {feedback.type === 'success' ? (
              <CheckCircle2 className="h-4 w-4" />
            ) : (
              <AlertCircle className="h-4 w-4" />
            )}
            <AlertDescription>{feedback.message}</AlertDescription>
          </Alert>
        )}

        <div>
          <Button
            variant="ghost"
            className="w-full flex items-center justify-between"
            onClick={() => setShowHints(!showHints)}
          >
            <span>Hints</span>
            <ChevronDown className={`h-4 w-4 transform transition-transform ${showHints ? 'rotate-180' : ''}`} />
          </Button>
          
          {showHints && exercise?.hints && (
            <div className="mt-2 p-4 bg-gray-50 rounded-lg space-y-2">
              {exercise.hints.map((hint: string, index: number) => (
                <div key={index} className="flex items-start gap-2">
                  <HelpCircle className="h-4 w-4 mt-1 flex-shrink-0" />
                  <p>{hint}</p>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>Attempts</span>
            <span>{attempts}</span>
          </div>
          <Progress value={Math.min(attempts * 20, 100)} />
        </div>
      </CardContent>

      <CardFooter>
        <Button
          variant="outline"
          onClick={fetchExercise}
          className="w-full"
        >
          Next Exercise
        </Button>
      </CardFooter>
    </Card>
  );
};

export default ExerciseComponent;
