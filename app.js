import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function App() {
  const [level, setLevel] = useState(1);
  const [xp, setXp] = useState(0);
  const [strength, setStrength] = useState(10);
  const [agility, setAgility] = useState(10);

  const completeWorkout = () => {
    const newXp = xp + 50;
    if (newXp >= 100) {
      setLevel(level + 1);
      setXp(0);
      setStrength(strength + 2);
      alert('🎉 LEVEL UP! مستوى ' + (level + 1));
    } else {
      setXp(newXp);
    }
  };

  const completeRun = () => {
    const newXp = xp + 30;
    setAgility(agility + 1);
    if (newXp >= 100) {
      setLevel(level + 1);
      setXp(0);
      alert('🎉 LEVEL UP! مستوى ' + (level + 1));
    } else {
      setXp(newXp);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>⚔️ Solo Fitness</Text>
      
      <View style={styles.card}>
        <Text style={styles.level}>مستوى {level}</Text>
        <Text style={styles.xp}>XP: {xp}/100</Text>
      </View>

      <View style={styles.statsContainer}>
        <Text style={styles.stat}>💪 قوة: {strength}</Text>
        <Text style={styles.stat}>🏃 سرعة: {agility}</Text>
      </View>

      <TouchableOpacity style={[styles.button, {backgroundColor: '#9b59b6'}]} onPress={completeWorkout}>
        <Text style={styles.buttonText}>💪 تمرين قوة (+50 XP)</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.button, {backgroundColor: '#3498db'}]} onPress={completeRun}>
        <Text style={styles.buttonText}>🏃 جري (+30 XP)</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a2e',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    color: '#9b59b6',
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 30,
  },
  card: {
    backgroundColor: '#16213e',
    padding: 20,
    borderRadius: 15,
    alignItems: 'center',
    marginBottom: 20,
    borderWidth: 2,
    borderColor: '#f1c40f',
    width: '80%',
  },
  level: {
    color: '#f1c40f',
    fontSize: 28,
    fontWeight: 'bold',
  },
  xp: {
    color: '#fff',
    fontSize: 18,
    marginTop: 5,
  },
  statsContainer: {
    flexDirection: 'row',
    marginBottom: 30,
  },
  stat: {
    color: '#fff',
    fontSize: 20,
    marginHorizontal: 15,
  },
  button: {
    padding: 18,
    borderRadius: 12,
    marginVertical: 10,
    width: '80%',
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
