// ============================================
// AKTU Results - Calculator Scripts
// ============================================

// SGPA to CGPA Calculator
function calculateCGPA() {
  const semester1 = parseFloat(document.getElementById('sem1').value) || 0;
  const semester2 = parseFloat(document.getElementById('sem2').value) || 0;
  const semester3 = parseFloat(document.getElementById('sem3').value) || 0;
  const semester4 = parseFloat(document.getElementById('sem4').value) || 0;
  const semester5 = parseFloat(document.getElementById('sem5').value) || 0;
  const semester6 = parseFloat(document.getElementById('sem6').value) || 0;
  const semester7 = parseFloat(document.getElementById('sem7').value) || 0;
  const semester8 = parseFloat(document.getElementById('sem8').value) || 0;
  
  const semesters = [semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8];
  const validSemesters = semesters.filter(s => s > 0);
  
  if (validSemesters.length === 0) {
    alert('Please enter at least one semester SGPA');
    return;
  }
  
  const total = validSemesters.reduce((sum, sgpa) => sum + sgpa, 0);
  const cgpa = (total / validSemesters.length).toFixed(2);
  
  document.getElementById('cgpaResult').textContent = cgpa;
  document.getElementById('totalSemesters').textContent = validSemesters.length;
  document.querySelector('.result-box').classList.add('show');
  
  // Scroll to result
  document.querySelector('.result-box').scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// CGPA to Percentage Calculator
function calculatePercentage() {
  const cgpa = parseFloat(document.getElementById('cgpaInput').value);
  
  if (!cgpa || cgpa < 0 || cgpa > 10) {
    alert('Please enter a valid CGPA between 0 and 10');
    return;
  }
  
  const percentage = (cgpa * 9.5).toFixed(2);
  
  document.getElementById('percentageResult').textContent = percentage + '%';
  document.getElementById('cgpaUsed').textContent = cgpa;
  document.querySelector('.result-box').classList.add('show');
  
  // Scroll to result
  document.querySelector('.result-box').scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Attendance Calculator
function calculateAttendance() {
  const totalClasses = parseInt(document.getElementById('totalClasses').value);
  const attendedClasses = parseInt(document.getElementById('attendedClasses').value);
  
  if (!totalClasses || !attendedClasses || totalClasses < 1 || attendedClasses < 0) {
    alert('Please enter valid numbers');
    return;
  }
  
  if (attendedClasses > totalClasses) {
    alert('Attended classes cannot be more than total classes');
    return;
  }
  
  const attendance = ((attendedClasses / totalClasses) * 100).toFixed(2);
  const classesNeeded = Math.max(0, Math.ceil((totalClasses * 0.75 - attendedClasses) / 0.25));
  const canSkip = Math.max(0, Math.floor((attendedClasses - totalClasses * 0.75) / 0.75));
  
  document.getElementById('attendanceResult').textContent = attendance + '%';
  document.getElementById('attendedCount').textContent = attendedClasses;
  document.getElementById('totalCount').textContent = totalClasses;
  
  const statusBox = document.getElementById('attendanceStatus');
  const extraInfo = document.getElementById('extraInfo');
  
  if (attendance >= 75) {
    statusBox.innerHTML = '<p style="color: #059669; font-weight: 600;">✓ You meet the minimum 75% requirement</p>';
    if (canSkip > 0) {
      extraInfo.innerHTML = `<p>You can skip up to <strong>${canSkip}</strong> more classes and still maintain 75% attendance.</p>`;
    } else {
      extraInfo.innerHTML = '<p>Continue attending classes to maintain your attendance.</p>';
    }
  } else {
    statusBox.innerHTML = '<p style="color: #DC2626; font-weight: 600;">✗ Below 75% requirement</p>';
    extraInfo.innerHTML = `<p>You need to attend <strong>${classesNeeded}</strong> consecutive classes to reach 75% attendance.</p>`;
  }
  
  document.querySelector('.result-box').classList.add('show');
  
  // Scroll to result
  document.querySelector('.result-box').scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Reset Functions
function resetCGPA() {
  document.querySelectorAll('.calculator-form input').forEach(input => input.value = '');
  document.querySelector('.result-box').classList.remove('show');
}

function resetPercentage() {
  document.querySelectorAll('.calculator-form input').forEach(input => input.value = '');
  document.querySelector('.result-box').classList.remove('show');
}

function resetAttendance() {
  document.querySelectorAll('.calculator-form input').forEach(input => input.value = '');
  document.querySelector('.result-box').classList.remove('show');
}
